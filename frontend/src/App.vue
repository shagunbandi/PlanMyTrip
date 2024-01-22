<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <nav>
    <h1><RouterLink to="/login">Login</RouterLink></h1>
    <h1><RouterLink to="/">Home</RouterLink></h1>
    <h1><RouterLink to="/about">About</RouterLink></h1>
    <hr />
  </nav>

  <RouterView />
</template>

<style>
@import 'bootstrap/dist/css/bootstrap.css';
</style>
