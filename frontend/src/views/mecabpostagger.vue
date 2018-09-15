<template>
    <div class="mecab">
        <div>
            <h2>
                Mecab 형태소 분석(Pos Tagger)
            </h2>
        </div>
        <div class="convertor">
            <div class="src">
                <textarea v-bind:id="src" v-model="srcText"  placeholder="Input Text" cols="50" rows="10"></textarea>
            </div>
            <div class="to">
                <button @click="removeImage(item)">분석</button>                <!--<img width="50" src="@/assets/arrow.png">-->
            </div>
            <div class="tgt">
                <textarea v-bind:id="tgt" v-model="tgtText"  placeholder="Output Text" cols="50" rows="10"></textarea>
            </div>
        </div>
    </div>


</template>

<style>
    .convertor {
        overflow: auto;
        height: auto;
    }

    .convertor > div {
        text-align: center;
        vertical-align: top;
        margin: auto;

        line-height:150px;
        display: inline-block;

    }

    .src {
        width:auto;
        height:auto;
        text-align:center;
    }

    .to {
        width:70px;
        text-align:center;
    }
</style>

<script>


    export default {
        name: 'mecabpostagger',

        data () {
            return {
                srcText: '',
                tgtText: ''
            }
        },
        created () {
            // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
            this.fetchData()
        },
        watch: {
            // 라우트가 변경되면 메소드를 다시 호출됩니다.
            '$route': 'fetchData'

        },
        methods: {
            fetchData () {
                this.tgtText ='adsf';
            }
        }
    }


</script>
