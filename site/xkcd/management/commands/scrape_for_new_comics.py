import re
import requests

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from xkcd.models import Comic


class Command(BaseCommand):
    def handle(self, *args, **options):
        res = requests.get('https://xkcd.com/archive/')
        res.raise_for_status()

        archive_soup = BeautifulSoup(res.text, features="html.parser")
        archives = archive_soup.find(id='middleContainer').find_all('a')

        stored_comics = Comic.objects.all().reverse()
        latest_stored = stored_comics[0] if stored_comics else None
        comics = []

        for comic in archives[:30]:
            number = comic.get('href').replace('/', '')

            # print(f'number {number}')
            if latest_stored and latest_stored.number == comic.number:
                break

            try:
                img_filename = comic.text.lower().replace(' ', '_')
                img_link = f'https://imgs.xkcd.com/comics/{img_filename}.png'
                img_res = requests.get(img_link)
                img_res.raise_for_status()
                print(f'Found xkcd {number} at {img_filename}')

            except requests.exceptions.HTTPError:
                xkcd_page_link = f'https://xkcd.com/{number}/'
                xkcd_page_res = requests.get(xkcd_page_link)
                xkcd_page_res.raise_for_status()

                xkcd_page_soup = BeautifulSoup(xkcd_page_res.text, features="html.parser")
                xkcd_page_middle = xkcd_page_soup.find(id='middleContainer')

                try:
                    permalink_pattern = 'https://imgs.xkcd.com/comics/(.+).png'
                    img_filename = re.search(permalink_pattern, xkcd_page_middle.text).group(1)
                    print(f'Found xkcd {number} at a custom location: {img_filename}')

                except (requests.exceptions.HTTPError, AttributeError) as e:
                    print(f'xkcd {number} not found: {e}')

            comics.append(Comic(
                number = number,
                published = comic.get('title'),
                display_name = comic.text,
                img_filename = img_filename,
            ))

        Comic.objects.bulk_create(comics)
