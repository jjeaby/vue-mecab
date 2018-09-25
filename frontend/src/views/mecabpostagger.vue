<template>
    <div class="mecab">
        <TextAreaConverter title="Mecab Pos Tagger (형태소 분석)" url="http://mecab.jjeaby.ml/api/mecabpos"/>
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
    },
};
</script>
