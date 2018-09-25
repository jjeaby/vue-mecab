<template>
    <div class="mecabspacecheck">
        <TextAreaConverter title="Mecab 띄어쓰기 (Space Check)" url="/api/mecabspace"/>
    </div>
</template>
<style>
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
