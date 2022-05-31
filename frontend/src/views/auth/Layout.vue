<template>
  <div class="auth">
    <div class="container">
      <div class="d-flex align-items-center row justify-content-center" style="height: 100vh">
        <div class="col-md-6">
          <div class="auth-box-right">
            <div class="card">
              <div class="card-body">
                <router-view></router-view>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: "Layout",
  mounted() {
    console.log('hello')
  }
}
</script>

<style scoped>

</style>