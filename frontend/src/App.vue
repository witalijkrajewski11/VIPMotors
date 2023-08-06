<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><span style="color: goldenrod"><b>VIP</b></span>Motors</router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <div class="dropdown is-hoverable">
          <div class="dropdown-trigger">
            <button class="button is-black" aria-haspopup="true" aria-controls="dropdown-menu">
              <span>New Cars</span>
              <span class="icon is-small">
                                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                                    </span>
            </button>
          </div>
          <div class="dropdown-menu" id="dropdown-menu" role="menu" style="overflow: hidden;">
            <div class="dropdown-content">
              <router-link class="dropdown-item custom-font-size custom-background" to="/new-cars">View all options</router-link>
              <router-link class="dropdown-item custom-font-size custom-background" to="/build-new-car">Build you favourite car</router-link>
            </div>
          </div>
        </div>

        <router-link to="/used-cars" class="navbar-item" style="color: white">Used Cars</router-link>
        <router-link to="/sell-your-car" class="navbar-item" style="color: white">Sell Your Car</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field has-addons">
            <div class="control">
              <input class="input is-rounded" type="text" placeholder="Search">
            </div>
            <div class="control">
              <button class="button is-rounded" style="color: black">
                <span class="icon">
                  <i class="fas fa-search"></i>
                </span>
              </button>
            </div>
          </div>
        </div>

        <div class="navbar-item">
          <router-link to="/favourites">
           <span class="icon">
              <i class="fas fa-heart"></i>
            </span>
          </router-link>
        </div>

        <div class="navbar-item">
          <router-link to="/cart">
           <span class="icon">
              <i class="fas fa-shopping-cart"></i>
            </span>
          </router-link>
        </div>

        <div class="navbar-item">
          <router-link to="/cart">
           <span class="icon">
              <i class="fas fa-user-circle"></i>
            </span>
          </router-link>
        </div>

      </div>
    </div>
  </nav>
  <router-view/>
</template>

<style scoped lang="scss">
@import "bulma";

.navbar {
  background-color: black;
  color: white;
}

.navbar-brand a {
  color: white;
}

.navbar-menu {
  background-color: black;
}

.navbar-item a {
  color: white;
  margin-right: 10px;
}

.field {
  margin: 0;
}

.input {
  background-color: #fff;
  color: #000;
}

.button.is-primary {
  background-color: #00d1b2;
}

.button.is-danger {
  background-color: #ff3860;
}

.dropdown-item:hover {
  text-align: inherit;
  white-space: nowrap;
}

.custom-font-size {
  font-size: 18px;
}

.custom-background {
  background-color: black;
  color: white;
}

</style>
<script setup>
</script>