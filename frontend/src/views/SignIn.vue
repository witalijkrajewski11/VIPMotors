<template>
  <main>
    <section class="section-login">
      <div class="section-main">
        <div class="section-login-1">
          <div class="section-login-1-main">

            <h1 class="section-login-1-title" style="color: black;"><span style="color: goldenrod">VIP</span>Motors</h1>
            <p class="section-login-1-text" style="color: black; margin-bottom: 7rem">Driving Excellence, Embracing
              Luxury</p>
            <div class="section-login-1-img" style=" margin-bottom: 13rem">
              <img
                  src="@/components/images/signUp.png"
                  alt="image">
            </div>

          </div>
        </div>
        <div class="section-login-2">
          <div class="section-login-2-main">

            <h1 class="section-login-2-title">Sign In</h1>
            <form class="section-login-2-form" @submit.prevent="signIn">
              <div class="login-form-1">
                <label for="input-email">Email</label>
                <input type="email" id="input-email" required minlength="8" v-model="email">
              </div>
              <div class="login-form-2">
                <label for="input-password">Password</label>
                <input type="password" id="input-password" required minlength="8" v-model="password">
              </div>
              <div class="login-form-submit-btn">
                <button type="submit">Sign In</button>
              </div>
              <div class="login-form-5">
                <p>Don't have an account?
                  <router-link to="/sign-up">Sign Up</router-link>
                </p>
              </div>
            </form>

          </div>
        </div>
      </div>
    </section>
  </main>
</template>


<script>
import axios from "axios";
import {useToast} from "vue-toastification";

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  setup() {
    const toast = useToast();
    return {toast}
  },
  methods: {
    signIn() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem("token")
      axios
          .post('api/token/', {'username': this.email, 'password': this.password})
          .then(res => {
            console.log(res)
            const token = res.data.access
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = 'Token ' + token;
            this.$router.push('/')
            this.toast.success('You successfully logged in!')

          }).catch(e => {
            console.log(e)
            if (e) {
              if (e.response.data.type === 'not_confirmed') {
                this.$router.push({name: 'ConfirmEmail', query: {email: this.email}})
              }
              if (e.response) {
                for (const property in e.response.data) {
                  if (property === 'non_field_errors') {
                    this.toast.error(`${e.response.data[property]}`)
                    continue;
                  }
                  this.toast.error(`${property}: ${e.response.data[property]}`)
                }
              } else {
                this.toast.error('Something went wrong. Please try again later.')
                console.log(JSON.stringify(e))
              }
            }
      })
    }
  },
  mounted() {
    document.title = 'SignIn | VIPMotors'
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap');

* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  font-family: 'DM Sans', sans-serif;
}

body {
  width: 100%;
  height: auto;
}


main section.section-login {
  width: 100%;
  height: 100vh;
  background-color: #455154;
//background: url(https://rvs-gradie-signup-page.vercel.app/Assets/Background.png); background-repeat: no-repeat; background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

main section.section-login .section-main {
  width: 60%;
  height: auto;
  display: flex;
}

main section.section-login .section-main .section-login-1, main section.section-login .section-login-2 {
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #fff;
}

main section.section-login .section-main .section-login-1 .section-login-1-main {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding-top: 50px;
}

main section.section-login .section-main .section-login-1 .section-login-1-main .section-login-1-title {
  font-size: 32px;
  color: #fff;
}

main section.section-login .section-main .section-login-1 .section-login-1-main .section-login-1-text {

  color: #ffffff94;

  font-size: 18px;
}

main section.section-login .section-main .section-login-1 .section-login-1-main .section-login-1-img {

  width: 100%;
}

main section.section-login .section-main .section-login-1 .section-login-1-main .section-login-1-img img {

  width: 100%;

  display: block;
}


main section.section-login .section-main .section-login-2 .section-login-2-main {
  width: 100%;
  height: 100%;
  background: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-title {
  font-size: 32px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form {
  margin-top: 25px;
  display: flex;
  flex-direction: column;
  row-gap: 20px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-1, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-2, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-3 {
  display: flex;
  flex-direction: column;
  row-gap: 8px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-1 label, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-2 label, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-3 label {
  font-weight: 500;
  font-size: 15px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-1 input, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-2 input, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-3 input {
  padding: 12px 15px;
  border: 1px solid #e9e6e6;
  border-radius: 4px;
  outline: none;
  font-size: 16px;
  width: 100%;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-4 {
  display: flex;
  column-gap: 7px;
  align-items: center;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-4 p, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-5 p {
  font-size: 14px;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-4 p a, main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-5 p a {
  font-weight: bold;
//color: #5a1fe0;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-submit-btn button {
  background: green;
  padding: 14px;
  width: 100%;
  color: #fff;
  outline: none;
  border: 0px;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
}

main section.section-login .section-main .section-login-2 .section-login-2-main .section-login-2-form .login-form-5 p {
  text-align: center;
}


@media only screen and (max-width: 1200px) {

  /* login page */
  main section.section-login .section-login-1 .section-login-1-main, main section.section-login .section-login-2 .section-login-2-main {
    width: 85%;
  }

  main section.section-login .section-login-1 .section-login-1-main .section-login-1-title, main section.section-login .section-login-1 .section-login-1-main .section-login-1-form {
    margin-top: 35px;
  }

  main section.section-login .section-main {
    width: 75%
  }

}

@media only screen and (max-width: 900px) {

  /* login page */
  main section.section-login .section-main {
    padding: 35px 0px;
  }

  main section.section-login .section-login-1 .section-login-1-main, main section.section-login .section-login-2 .section-login-2-main {
    width: 90%;
  }

  main section.section-login .section-login-1 .section-login-1-main {
    height: 90%;
  }

  main section.section-login .section-login-1 .section-login-1-main .section-login-1-title, main section.section-login .section-login-1 .section-login-1-main .section-login-1-form {
    margin-top: 25px;
  }

  main section.section-login .section-main {
    flex-direction: column;
    width: 75%;
    padding: 50px 0px;
  }

  main section.section-login .section-main .section-login-1, main section.section-login .section-login-2 {
    width: 100%;
  }

  main section.section-login {
    height: unset;
  }
}

@media only screen and (max-width: 600px) {
  main section.section-login .section-main {
    width: 100%;
    padding: 0px;
  }

  main section.section-login .section-main .section-login-2 .section-login-2-main {
    padding: 35px 25px;
  }
}
</style>