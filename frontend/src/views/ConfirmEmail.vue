<template>
  <div class="container has-text-centered">
    <div class="square">
      <h2><span style="color: goldenrod"><b>VIP</b></span>Motors</h2><br><br><br>

      <h3>Confirm Your email please:<br>{{email}}</h3><br><br><br><br><br><br><br><br><br>

      <p>Have some questions? Reach out our support center:</p>
      <span><a style="text-decoration: none; color: coral" href="mailto:vipmotors-support@gmail.com">Contact us</a></span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ConfirmEmail",
  data() {
    return {
      email: this.$route.query.email
    }
  },
  mounted() {
    document.title = 'Confirm Email | VIPMotors'
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #455154;
  height: 100vh;
}

.square {
  width: 700px;
  height: 500px;
  background-color: #fff;
  //display: flex;
  //justify-content: center;
  //align-items: center;
}

.text {
  color: white;
  font-size: 24px;
  font-weight: bold;
}
</style>