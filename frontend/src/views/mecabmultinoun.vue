<template id="app">
    <div class="mecabspace" >
        <div class="textarea">
            <TextAreaConverter title="키워드 추출" url="/api/mecabmultinoun"/>
        </div>
    </div>

</template>

<style>
    .mecabspace {
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

    name: 'mecabmultinoun',
    components: {
        TextAreaConverter,
    },
};
</script>
