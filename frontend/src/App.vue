<template>
  <div id="app">
    <div id="nav">
      <router-link to="/mecabpos">Mecab 형태소 분석</router-link> |
      <router-link to="/mecabspacing">Mecab 띠어쓰기</router-link> |
      <router-link to="/">About</router-link>
    </div>
    <router-view/>
  </div>
</template>
<style lang="scss">
  // I had to import main scss file in every .vue component. Otherwise the `$vue-green` is undefined when bunddling.
  @import './styles/common';
</style>

