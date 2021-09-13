<template>
  <div v-if="showMenu" class="d-flex menu-right pa-4" @mouseleave="cancel">
    <v-icon color="red darken-1" class="close" @click="cancel"
      >mdi-window-close</v-icon
    >
    <h3 class="mt-3">{{ header }}</h3>
    <slot></slot>
  </div>
</template>
 
<script>
export default {
  props: ["header", "showMenu"],
  methods: {
    cancel() {
        this.$emit('close')
    },
  },
};
</script>
 
<style lang="scss" scoped>
.menu-right {
  flex-direction: column;
  position: relative;
  z-index: 1100;
  background-color: #e8e8e8;
  width: 230px;
  overflow-y: auto;
 
  transition: transform 0.3s, opacity 0.3s;
  .close {
    position: absolute;
    top: 8px;
    right: 8px;
  }
  .list {
    padding-left: 0;
    flex-direction: column;
    list-style: none;
    width: 100%;
  }
  h3 {
      font-size: 25px;
  }
}
</style>