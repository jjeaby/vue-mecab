<template>
    <div id="app">
        <div id="nav">
            <router-link to="/mecabpostagger">Mecab 형태소 분석</router-link>
            |
            <router-link to="/mecabspacecheck">Mecab 띄어쓰기 체크</router-link>
            |
            <router-link to="/about">About</router-link>
        </div>
        <router-view/>
    </div>
</template>

<style lang="scss">
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        width: 100%;
        justify-content: center;
        padding: 30px;
        a {
            font-weight: bold;
            color: #2c3e50;
            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }
</style>
