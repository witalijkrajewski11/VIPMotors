<template>
  <div class="container has-text-centered">
    <div class="square">
      <h2><span style="color: goldenrod"><b>VIP</b></span>Motors</h2><br><br><br>
      <h3>Thanks for confirmation!</h3><br><br><br>
      <h4>You'll be redirected to VIPMotors in {{ countdown }} seconds</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmailConfirmed",
  data() {
    return {
      countdown: 5
    };
  },
  mounted() {
    this.startCountdown();
    document.title = 'Thanks For Confirmation | VIPMotors'
  },
  methods: {
    startCountdown() {
      let timer = setInterval(() => {
        this.countdown--;
        if (this.countdown === 0) {
          clearInterval(timer);
          this.redirectToHomePage();
        }
      }, 1000);
    },
    redirectToHomePage() {
      this.$router.push("/");
    }
  },
};
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
}

.text {
  color: white;
  font-size: 24px;
  font-weight: bold;
}
</style>