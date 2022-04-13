<template>
  <form @submit.prevent="login">
    <div class="form-head">
      <a href="index.html" class="logo"><img
          src="http://themesbox.in/admin-templates/gappa/html/light/assets/images/logo.svg" class="img-fluid"
          alt="logo"></a>
    </div>
    <h4 class="text-primary my-4">Log in !</h4>


    <div class="form-floating mb-3">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Username</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <div class="row justify-content-end">
      <div class="col-md-6">
        <router-link class="float-end mb-3" to="forget-password">Forgot Password ?</router-link>
      </div>
    </div>

    <div class="d-grid gap-2">
      <button class="btn btn-success btn-lg btn-block font-18" type="submit">Log in</button>
    </div>
  </form>

  <p class="mb-0 mt-3">Don't have a account?
    <router-link to="/registration">Create an account</router-link>
  </p>

</template>

<script>
export default {
  name: "Login",
  methods: {
    login() {
      this.$router.replace({path: '/app'})
    }
  }
}
</script>

<style scoped>

</style>