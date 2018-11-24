<template>
  <div id="app">
    <Comic
      v-for="comic in comics"
      v-bind:key="comic.xkcd"
      v-bind:xkcd="comic"
    ></Comic>
  </div>
</template>

<script>
import axios from 'axios'
import Comic from './Comic'

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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
