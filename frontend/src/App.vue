<template>
  <div>
    <nav class="navbar navbar-light bg-light">
      <div class="container">
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/login">Login</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/about">Itinerary</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
    <br />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
