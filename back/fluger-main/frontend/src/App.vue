<template>
  <v-app>
    <v-main>
      <app-menu />
      <v-container>
        <transition
          name="fade"
          mode="out-in"
          @beforeLeave="beforeLeave"
          @enter="enter"
          @afterEnter="afterEnter"
        >
          <router-view />
        </transition>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import appMenu from "./components/menu/Menu.vue"

export default {
  name: "App",

  data() {
    return {
      activeTab: undefined,
      prevHeight: 0,
    };
  },
  components: {
    appMenu,
  },
  methods: {
    beforeLeave(element) {
      this.prevHeight = getComputedStyle(element).height;
    },
    enter(element) {
      const { height } = getComputedStyle(element);

      element.style.height = this.prevHeight;

      setTimeout(() => {
        element.style.height = height;
      });
    },
    afterEnter(element) {
      element.style.height = "auto";
    },
  },
};
</script>

<style lang="scss"> 
#app {
  min-height: 100vh;
  font-family: "Golos-UI", sans-serif;
}
@font-face {
  font-family: "Golos-UI";
  src: local("Golos UI"), local("Golos-UI"),
    url("~@/assets/fonts/Golos-UI/Golos-UI_Regular.woff") format("woff"),
    url("~@/assets/fonts/Golos-UI/Golos-UI_Regular.woff2") format("woff2");
  font-weight: 100;
  font-style: normal;
}
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-property: height, opacity;
  transition-timing-function: ease;
  overflow: hidden;
}
.pointer {
  cursor: pointer;
}
</style>
