<template>
    <div id="app" class="app">
        <div id="nav" class="nav">
            <router-link to="/mecabpostagger">Mecab 형태소</router-link>
            |
            <router-link to="/mecabspacecheck">Mecab 띄어쓰기</router-link>
            |
            <router-link to="/mecabmultinoun">키워드 추출</router-link>
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
        padding: 30px;
        display: inline-block;
        a {
            font-weight: bold;
            color: #2c3e50;
            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }
    @media all and (max-width: 900px) {
        .nav {
            margin: 0 auto;
            display: block
        }

    }
</style>
