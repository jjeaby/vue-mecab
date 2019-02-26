<template>
    <div class="center">
        <TextAreaConverter title="Mecab 띄어쓰기 (Space Check)" url="/api/mecabspace"/>
    </div>
</template>
<style>
    .center {
        margin: auto;
        width: 50%;
        padding: 10px;
    }
    .mecabspacecheck {
        padding: 20px;
        justify-content: center;
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
