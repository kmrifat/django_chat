<template>

  <section v-if="selected_user">
    <active-user :user="selected_user"></active-user>

    <div class="chat-body" ref="chatBody">
      <div v-for="message in selected_user.messages" class="chat-message"
           :class="message.sender_id === 'me' ? 'right': 'left'">
        <div class="text">
          <span>{{ message.text }}</span>
        </div>
        <div class="meta">
          <span>{{ message.date_time }}</span>
          <i class="feather icon-check ml-2"></i>
        </div>
      </div>
    </div>

    <div class="chat-bottom">
      <div class="chat-messagebar">
        <form @submit.prevent="sendMessage">
          <div class="input-group">
            <div class="input-group-prepend">
              <a href="#" id="button-addonmic"><i class="feather icon-mic"></i></a>
            </div>
            <input v-model="message" type="text" class="form-control" placeholder="Type a message..." aria-label="Text">
            <div class="input-group-append">
              <a href="#" class="mr-3" id="button-addonlink"><i class="feather icon-paperclip"></i></a>
              <a href="#" id="button-addonsend"><i class="feather icon-send"></i></a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>

  <section v-else>
    Show default message
  </section>

</template>

<script>
import ActiveUser from "./ActiveUser.vue";

export default {
  name: "MessageWindow",
  props: ['selected_user'],
  components: {
    'active-user': ActiveUser
  },
  data() {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage() {
      this.selected_user.messages.push({
        text: this.message,
        read: false,
        date_time: 'now',
        sender_id: 'me'
      })
      this.message = ''
      this.scrollDown()
    },

    scrollDown() {
      this.$refs.chatBody.scrollTo(0, this.$refs.chatBody.scrollHeight)
    }
  },
  mounted() {
    this.scrollDown()
  }
}
</script>

<style scoped>

</style>