<template>
  <button @click="toggleLocalAudio" class="btn btn-lg btn-secondary rounded-circle mx-1">
    <i :class="icon"></i>
  </button>
</template>

<script>
export default {
  name: "MicButton",
  data() {
    return {
      stashed: false,
      icon: 'fa-solid fa-microphone'
    }
  },
  props: {
    clickCallback: {
      type: Function
    }
  },
  methods: {
    toggleLocalAudio() {
      if (!this.stashed) {
        this.icon += '-slash'
      } else {
        this.icon = 'fa-solid fa-microphone'
      }
      this.stashed = !this.stashed
      this.clickCallback()
    }
  }
}
</script>

<style scoped>

</style>