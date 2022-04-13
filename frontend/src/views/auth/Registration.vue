<template>
  <form @submit.prevent="register">
    <div class="form-head">
      <a href="index.html" class="logo"><img
          src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/logo.svg" class="img-fluid"
          alt="logo"></a>
    </div>
    <h4 class="text-primary my-4">Create an Account</h4>


    <div class="form-floating mb-3">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Username</label>
    </div>

    <div class="form-floating mb-3">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">First Name</label>
    </div>

    <div class="form-floating mb-3">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Last Name</label>
    </div>

    <div class="form-floating mb-3">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>


    <div class="d-grid gap-2">
      <button class="btn btn-success btn-lg btn-block font-18" type="submit">Sign up</button>
    </div>
  </form>

  <p class="mb-0 mt-3">Already have an account?
    <router-link to="/">Log in</router-link>
  </p>
</template>

<script>
export default {
  name: "Registration",
  methods: {
    register() {
      this.$router.replace('/app')
    }
  }
}
</script>

<style scoped>

</style>