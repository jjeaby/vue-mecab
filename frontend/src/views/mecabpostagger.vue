<template id="app">
    <div class="mecabpostagger" >
        <div class="textarea">
            <TextAreaConverter   title="Mecab 형태소 분석 (Pos Tagger)" url="/api/mecabpos"/>
        </div>
    </div>

</template>
<style>
    .mecabpostagger {
        text-align: center;
    }
    .textarea {
        font-size: 15px;
        text-align: center;
        display: inline-block;
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
