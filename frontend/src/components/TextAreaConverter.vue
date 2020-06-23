<template>
    <div class="TextAreaConverter">

        <div class="center">
            <div><h2>{{ title }}</h2></div>
        </div>

            <div class="center2" v-if="checkSizes === 'grid'">
                    <div class="grid" >
                        <div class="cell">
                        <textarea v-model="srcText" placeholder="Input Text"
                                  cols="48" rows="20"></textarea>
                        </div>
                        <div class="cellBtn">
                            <button class="button" @click="mecabPos()">분석</button>
                            <button class="button" @click="mecabPosReset()">리셋</button>
                        </div>
                        <div class="cell">
                    <textarea v-model="tgtText" readonly placeholder="Output Text"
                              cols="48" rows="20"></textarea>
                        </div>
                    </div>
                </div>
            <div class="center2" v-else>
            <div class="table" >
                <div style="display: table-row;">
                <div style="display: table-cell;" >
                        <textarea v-model="srcText" placeholder="Input Text"
                                  cols="48" rows="20"></textarea>
                </div>
                <div style="display: table-cell; vertical-align: middle;" >
                    <button class="button" @click="mecabPos()">분석</button>
                    <br>
                    <button class="button" @click="mecabPosReset()">리셋</button>
                </div>
                <div style="display: table-cell;" >
                   <textarea v-model="tgtText" readonly placeholder="Output Text"
                              cols="48" rows="20"></textarea>
                </div>
                </div>
            </div>
        </div>


    </div>
</template>

<style scoped lang="scss">
    .TextAreaConverter {
        /*border-style: solid;*/

    }
    .center {
        margin: auto;
        width: inherit;
        padding: 10px;
    }

    .center2 {
        /*border-style: solid;*/
        position: relative;
        padding: 10px;

    }

    .table {
        display:  table;
    }

    .block {
        display: inline-block;
    }
    .grid {
        display: inline-grid;
    }
    .cell {
        width: inherit;

    }
    .cellBtn {
        display: inline-block;
        width: inherit;
        vertical-align: middle;
        padding: 5px;
    }
    .button {
        padding: 5px; margin: 5px;
    }
</style>

<script>
import axios from 'axios';

export default {
    name: 'TextAreaConverter',
    props: {
        title: String,
        url: String,
    },
    data() {
        return {
            srcText: '',
            tgtText: '',
            layout: 'cell',
            error: [],
        };
    },
    computed: {
        checkSizes() {
            return this.layout;
        },
    },
    created() {
        // 뷰가 생성되고 데이터가 이미 감시 되고 있을 때 데이터를 가져온다.
        // this.mecabPos();
        this.resize();
        window.addEventListener('resize', this.resize);
    },

    update() {

    },
    destroyed() {
        window.removeEventListener('resize', this.resize);
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
            axios.post(this.url, requestData)
            // axios.post('http://localhost:38080/api/mecabmultinoun', requestData)
                .then((response) => {
                    // JSON responses are automatically parsed.
                    const responseData = response.data;

                    if (this.url === '/api/mecabspace') {
                        this.tgtText = responseData;
                    } else {
                        const responseDataJson = JSON.stringify(responseData);
                        this.tgtText = JSON.stringify(JSON.parse(responseDataJson), null, 2);
                    }
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


        resize() {
            const width = window.innerWidth;
            console.log(width);
            if (width > 900) this.layout = 'cell';
            else this.layout = 'grid';
        },
    },
};

</script>
