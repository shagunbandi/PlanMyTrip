<script>
import { RouterLink } from 'vue-router'
import NavigationSide from '../components/NavigationSide.vue'

export default {
    name: 'HomeView',
    components: {
        RouterLink,
        NavigationSide
    }
  }

</script>

<template>
    <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <NavigationSide />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/plan">Plan</RouterLink>
        <RouterLink to="/some-action">some action</RouterLink>
      </nav>
    </div>
  </header>

  <h1>Made with ❤️ by Shagun Bandi</h1>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
