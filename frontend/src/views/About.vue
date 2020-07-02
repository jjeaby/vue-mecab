<template id="app">
    <div class="about" >
        <div class="infomation">
            <h1>{{a}}</h1>
            <div style="text-align: center">
            Mecab 을 Base 로 하여 한글 띄어쓰기를 검사 할 수 있으며, <br>
            Mecab 을 설치 하지 않고 어떤 형태로 형태소가 분석되는지 <br>
            텍스트의 키워드가 어떤 것인지 <br>
            확인 할 수 있습니다.<br>
            <br>
            문의는 <b>jjeaby@gmail.com</b> 으로 메일 주시면 좋겠네요!

            </div>
        </div>
    </div>

</template>
<style>
    .about {
        text-align: center;
    }
    .infomation {
        font-size: 15px;
        text-align: center;
        display: inline-block;
    }

</style>


<script>


export default {
    name: 'about',
    data() {
        return {
            a: '한글 형태소 분석, 띠어쓰기 체크 서비스',
        };
    },
    created() {
        // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
        this.fetchData();
    },
    watch: {
        // 라우트가 변경되면 메소드를 다시 호출됩니다.
        $route: 'fetchData',
    },
    methods: {
        fetchData() {

        },
    },
};


</script>
