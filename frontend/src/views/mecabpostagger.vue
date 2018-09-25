<template>
    <div class="mecab">
        <h1 class="title">Mecab Pos Tagger(형태소 분석)</h1>
        <table class="tbl">
            <caption>Mecab Pos Tagger(형태소 분석)</caption>
            <colgroup>
                <col style="width: 400px;">
                <col style="width: 80px;">
                <col style="width: 400px;">
            </colgroup>

            <tr>
                <th scope="col">
                    <textarea v-model="srcText" placeholder="Input Text" cols="40" rows="20"></textarea>
                </th>
                <th scope="col">
                    <button @click="mecabPos()">분석</button>
                    <p/>
                    <button @click="mecabPosReset()">리셋</button>
                </th>
                <th scope="col">
                    <textarea v-model="tgtText" readonly placeholder="Output Text"
                              cols="40" rows="20"></textarea>
                </th>
            </tr>
        </table>
    </div>


</template>

<style>
    .mecab {
        padding: 20px;
        justify-content: center;
    }

    .title {
        font-family: "Roboto Slab", "ff-tisa-web-pro", "Georgia", Arial, sans-serif;
        font-size: x-large;
        font-style: normal;
    }

    .tbl {
        width: 100%;
        border-collapse: collapse;
        border-spacing: 0;
    }

    .tbl caption {
        overflow: hidden;
        position: absolute;
        width: 0;
        height: 0;
        line-height: 0;
        text-indent: -9999px
    }

    .tbl th {
        padding: 10px 0;
    }

    .tbl td {
        padding: 10px 0 10px 10px;
    }

    @media all and (max-width: 880px) {
        .tbl,
        .tbl thead,
        .tbl tbody,
        .tbl tr,
        .tbl th,
        .tbl td {
            display: block
        }

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

            // axios.post('http://mecab.jjeaby.ml/api/mecabpos', requestData)
            axios.post('http://localhost:18080/api/mecabpos', requestData)
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
