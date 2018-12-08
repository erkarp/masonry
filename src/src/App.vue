<template>
  <div id="app">
    <main v-masonry item-selector=".comic"
      transition-duration="0.3s">
      <Comic
        v-for="comic in comics"
        v-bind:key="comic.xkcd"
        v-bind:xkcd="comic"
        v-on:click.native="openModal(comic)"
        v-masonry-tile class="comic"
      ></Comic>
    </main>

    <Modal
      v-if="comicModal"
      v-bind:xkcd="comicModal"
      @close="closeModal"
    ></Modal>

    <sub v-if="moreToLoad">Loading…</sub>
    <sub v-else>You have finished xkcd.</sub>
  </div>
</template>

<script>
import {VueMasonryPlugin} from 'vue-masonry'
import axios from 'axios'
import Vue from 'vue'
import Comic from './components/Comic'
import Modal from './components/Modal'

Vue.use(VueMasonryPlugin)

export default {
  name: 'App',
  components: { Comic, Modal },
  data () {
    return {
      comics: [],
      page: 0,
      moreToLoad: true,
      comicModal: null
    }
  },
  methods: {
    initScrollListener () {
      const _this = this

      window.onscroll = () => {
        const d = document.documentElement
        if (d.scrollHeight - d.scrollTop === d.clientHeight) {
          _this.fetchComics()
        }
      }
    },
    fetchComics () {
      const _this = this

      axios.get(`http://127.0.0.1:8000/xkcds/?page=${++_this.page}`)
        .then(response => {
          if (response.data.comics) {
            _this.comics = _this.comics.concat(response.data.comics)
            _this.page = response.data.page
          } else {
            _this.moreToLoad = false
          }
        })
    },
    openModal (comic) {
      this.comicModal = comic
    },
    closeModal () {
      this.comicModal = null
    }
  },
  mounted () {
    this.fetchComics()
    this.initScrollListener()
  }
}
</script>

<style>
body {
  background-color: cornflowerblue;
  height: calc(100vh + 5px);
  margin-bottom: 5px;
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
sub {
  margin: 50px 0;
}
</style>
