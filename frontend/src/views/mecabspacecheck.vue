<template id="app">
    <div class="mecabspace" >
        <div class="textarea">
            <TextAreaConverter title="Mecab 띄어쓰기 (Space Check)" url="/api/mecabspace"/>
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

    name: 'mecabspacecheck',
    components: {
        TextAreaConverter,
    },
};
</script>
