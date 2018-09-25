<template>
    <div class="mecab">
        <h1 class="title">Mecab Pos Tagger(형태소 분석)</h1>

        <TextAreaConverter msg="Welcome to Your Vue.js App"/>


    </div>


</template>

<style>
    .mecab {
        padding: 20px;
        justify-content: center;
    }

</style>

<script>
import TextAreaConverter from '@/components/TextAreaConverter.vue';

export default {

    name: 'mecabpostagger',
    components: {
        TextAreaConverter,
    }
};


</script>
