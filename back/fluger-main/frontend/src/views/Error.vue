<template>
  <div class="d-flex body">
    <h2>Ошибка</h2>
    <h3>Такая страница не найдена :(</h3>
    <h3>А возможно её и не существовало.</h3>
    <i class="far fa-frown"></i>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.body {
  flex-direction: column;
}
.body h2,
h3 {
  text-align: center;
}
.sad-smile {
    width: 100px;
    height: 100px;
}
</style>