<template>
    <div class="center">
        <TextAreaConverter   title="Mecab 형태소 분석 (Pos Tagger)" url="/api/mecabpos"/>
    </div>
</template>
<style lang="scss" scoped>
    .center {
        margin: auto;
        width: 50%;
        padding: 10px;
    }
    /*.mecabpostagger {*/
        /*padding: 20px;*/
        /*justify-content: center;*/
    /*}*/

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
