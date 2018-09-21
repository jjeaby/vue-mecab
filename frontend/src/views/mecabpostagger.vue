<template>
    <div class="mecab">
        <div>
            <h2>
                Mecab 형태소 분석(Pos Tagger)
            </h2>
        </div>
        <div class="convertor">
            <div class="src">
                <textarea v-model="srcText" placeholder="Input Text" cols="50" rows="20"></textarea>
            </div>
            <div class="to">
                <div class="convertorBtn">
                    <div>
                        <button @click="mecabPos()">분석</button>
                    </div>
                    <div>&nbsp;</div>
                    <div >
                        <button @click="mecabPosReset()">리셋</button>

                    </div>
                </div>
            </div>
            <div class="tgt">
                <textarea v-model="tgtText" placeholder="Output Text" cols="50" rows="20"></textarea>
            </div>

        </div>
    </div>


</template>

<style>
    .convertorBtn {
        width: 150px;
        /*display: flex;*/
    }

    .convertorBtn > div {
        text-align: center;
        vertical-align: top;
        margin: auto;

    }

    .convertor {
        overflow: auto;
        display: inline;
        vertical-align: middle
    }

    .convertor > div {
        text-align: center;
        vertical-align: top;
        margin: auto;

        display: inline-block;
    }

    .src {
        width: 390px;
        height: auto;
        text-align: center;
    }

    .to {
        width: 130px;
        text-align: center;
    }

    .tgt {
        width: 390px;
        height: auto;
        text-align: left;
    }

    textarea {

    }
</style>

<script>

import axios from 'axios';

export default {
    name: 'mecabpostagger',

    data() {
        return {
            srcText: '',
            tgtText: '',
            error: [],
        };
    },
    created() {
        // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
        // this.mecabPos();
    },
    watch: {
        // 라우트가 변경되면 메소드를 다시 호출됩니다.
        // '$route': 'fetchData'
        // 'srcText': 'mecabPos'
    },
    methods: {
        // fetchData() {
        //     this.tgtText = 'adsf';
        // }
        mecabPos() {
            // this.tgtText = 'aaaa';
            const requestData = {};
            requestData.srcText = this.srcText;

            axios.post('http://svc.jjeaby.ml/api/mecabpos', requestData)
                .then((response) => {
                    // JSON responses are automatically parsed.
                    const responseData = response.data;
                    const responseDataJson = JSON.stringify(responseData);
                    this.tgtText = JSON.stringify(JSON.parse(responseDataJson), null, 2);
                })
                .catch((error) => {
                    console.log('errorType', typeof error);
                    console.log('error', Object.assign({}, error));
                });
        },
        mecabPosReset() {
            this.tgtText = '';
            this.srcText = '';
        },
    },
};


</script>
