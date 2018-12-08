<template>
  <figure>
    <img :src="permalink" :alt="this.xkcd.name">
    <figcaption>
      {{this.xkcd.name}}
      (<time :datetime="this.xkcd.date">{{this.xkcd.date}}</time>)
      <sub>{{this.xkcd.xkcd}}</sub>
    </figcaption>
  </figure>
</template>

<script>
export default {
  name: 'Comic',
  props: ['xkcd'],
  computed: {
    permalink: function () {
      return `https://imgs.xkcd.com/comics/${this.xkcd.file}`
    }
  }
}
</script>
