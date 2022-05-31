<template>

  <section v-if="selected_user">
    <active-user :user="selected_user"></active-user>

    <div class="chat-body" ref="chatBody">
      <div v-for="message in selected_user.messages" class="chat-message"
           :class="message.sender !== selected_user.username ? 'right': 'left'">
        <div class="text">
          <span>{{ message.text }}</span>
        </div>
        <div class="meta">
          <span>{{ dateHumanize(message.date_time) }}</span>
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
    <default-message-window></default-message-window>
  </section>

</template>

<script>
import ActiveUser from "./ActiveUser.vue";
import axios from "../../../../../axios";
import moment from "moment";
import DefaultMessageWindow from "../../../../../components/DefaultMessageWindow.vue";

export default {
  name: "MessageWindow",
  props: ['selected_user'],
  components: {
    'active-user': ActiveUser,
    'default-message-window': DefaultMessageWindow
  },
  data() {
    return {
      message: ''
    }
  },
  watch: {
    'selected_user.messages': {
      deep: true,
      handler() {
        if (this.$refs.hasOwnProperty('chatBody')) {
          this.scrollDown()
        }
      }
    }
  },
  methods: {
    sendMessage() {
      this.selected_user.messages.push({
        text: this.message,
        read: true,
        date_time: moment().format(),
        sender_id: 'me'
      })
      axios.post('message/', {
        text: this.message,
        receiver: this.selected_user.username
      }).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
      }).finally(e => {
        this.message = ''
      })
    },

    dateHumanize(date) {
      return moment(date).fromNow()
    },

    scrollDown() {
      this.$refs.chatBody.scrollTop = this.$refs.chatBody.scrollHeight
    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>