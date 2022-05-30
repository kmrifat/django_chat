<template>
  <div class="chat-head">
    <div class="row justify-content-between">
      <div class="col-6">
        <ul class="list-unstyled mb-0">
          <li class="media">
            <div v-if="user.online" class="user-status"></div>
            <img src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/girl.svg" alt="">
            <div class="media-body">
              <h5>{{ user.name }}</h5>
              <p class="mb-0">{{ user.online ? 'Online' : 'Offline' }}</p>
            </div>
          </li>
        </ul>
      </div>
      <div class="col-6">
        <ul class="list-inline float-end mb-0">
          <li class="list-inline-item">
            <button @click="makeCall" type="button" class="">
              <img src="/src/assets/icons/phone.svg" alt="">
            </button>
          </li>

          <li class="list-inline-item">
            <button @click="makeCall" type="button" class="">
              <img src="/src/assets/icons/video.svg" alt="">
            </button>
          </li>

          <li class="list-inline-item">
            <button type="button" class="">
              <img src="/src/assets/icons/more-vertical.svg" alt="">
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ActiveUser",
  props: ['user'],
  methods: {
    makeCall() {
      let routeData = this.$router.resolve({
        name: 'callerView',
        params: {
          username: this.$store.state.activeUser.username,
          receiver: this.user.username,
        },
        query: {
          display: JSON.stringify({
            username: this.user.username,
            photo: this.user.photo,
            name: this.user.name,
            online: this.user.online
          })
        }
      });
      window.open(routeData.href, '_blank', 'popup,height=650,width=550,resizable=0,location=no,toolbar=no,menubar=no,resizable=no')
      // window.open(routeData.href, '_blank')
    }
  }
}
</script>

<style scoped>

</style>