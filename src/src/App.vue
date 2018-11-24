<template>
  <div id="app" v-masonry
    item-selector=".comic"
    transition-duration="0.3s">
    <Comic
      v-for="comic in comics"
      v-bind:key="comic.xkcd"
      v-bind:xkcd="comic"
      v-masonry-tile class="comic"
    ></Comic>
  </div>
</template>

<script>
import {VueMasonryPlugin} from 'vue-masonry'
import axios from 'axios'
import Vue from 'vue'
import Comic from './Comic'

Vue.use(VueMasonryPlugin)

export default {
  name: 'App',
  components: { Comic },
  data () {
    return {
      comics: []
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/xkcds/')
      .then(response => (this.comics = response.data))
  }
}
</script>

<style>
body {
  background-color: cornflowerblue;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
.comic {
  max-width: 22%;
  margin: 10px;
}
img {
  max-width: 100%;
}
</style>
