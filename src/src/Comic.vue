<template>
  <figure>
    <img :src="comic_one" :alt="this.xkcd.name">
    <figcaption>
      {{this.xkcd.name}}
      (<date>{{this.xkcd.date}}</date>)
    </figcaption>
  </figure>
</template>

<script>
export default {
  name: 'Comic',
  props: ['xkcd'],
  computed: {
    comic_one: function () {
      return `https://imgs.xkcd.com/comics/${this.xkcd.link}.png`
    }
  }
}
</script>
