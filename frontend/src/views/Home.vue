<template id="app">
    <div class="home">
    </div>
</template>


<script>
    export default {
        name: 'home',

        data() {
            return {
                        // a: this.data.a,

            }
        },
        created() {

            // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
            // this.fetchData()
            this.fetchMoveToAbout()

        },
        watch: {
            // 라우트가 변경되면 메소드를 다시 호출됩니다.
            '$route': 'moveToAbout'
        },
        methods: {
            // fetchData() {         }
            fetchMoveToAbout() {
                this.$router.push({path: 'about'});
            }
        }
    }
</script>

