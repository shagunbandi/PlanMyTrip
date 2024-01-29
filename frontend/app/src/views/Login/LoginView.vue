<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <label for="username">Username:</label>
      <input v-model="username" type="text" id="username" required />
      <br />
      <label for="password">Password:</label>
      <input v-model="password" type="password" id="password" required />
      <br />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import api from '../../api'

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login() {
      api
        .post('/api/token/', {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          const token = response.data

          // Store the token in local storage or Vuex store
          localStorage.setItem('access', token.access)
          localStorage.setItem('refresh', token.refresh)
          this.$router.push('/')
        })
        .catch((error) => {
          console.error('Authentication failed', error)
          // Handle authentication failure (show error message, etc.)
        })
    },
  },
}
</script>

<style scoped>
/* Add your styling here if needed */
</style>
