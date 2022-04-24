<template>
  <div class="card">
    <div class="mt-5"></div>
    <img height="150" src="/src/assets/icons/girl.svg" class="rounded-circle" alt="">
    <div class="card-body">
      <div class="text-center">
        <h3>The User Name</h3>
      </div>
      <h6 class="text-center">Ringing...</h6>
    </div>
    <div class="card-footer">
      <div class="row justify-content-between">
        <button class="btn btn-primary col-4">Answer</button>
        <button class="btn btn-danger col-4">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CallView",
  data() {
    return {
      sender: '',
      receiver: ''
    }
  },
  methods: {},
  mounted() {
    this.receiver = JSON.parse(this.$route.query.receiver)
    this.sender = JSON.parse(this.$route.query.sender)
    // TODO: generate peer id
    // TODO: send the peer it to server using ajax
    // TODO: implement websocket
    // TODO:
  }
}
</script>

<style scoped>

</style>