<template>
  <button @click="toggleBtn" class="btn btn-lg btn-primary rounded-circle mx-1">
    <i :class="icon"></i>
  </button>
</template>

<script>
export default {
  name: "VideoButton",
  data() {
    return {
      stashed: false,
      icon: 'fa-solid fa-video'
    }
  },
  props: {
    clickCallback: {
      type: Function
    }
  },
  methods: {
    toggleBtn() {
      if (!this.stashed) {
        this.icon += '-slash'
      } else {
        this.icon = 'fa-solid fa-video'
      }
      this.stashed = !this.stashed
      this.clickCallback()
    }
  }
}
</script>

<style scoped>

</style>