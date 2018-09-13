<template>
    <div class="mecab">
        <textarea v-model="message" :placeholder="msg" cols="50" rows="10"></textarea>
    </div>
</template>

<script>
export default {
    name: 'MultilineMsgBox',
    props: {
        msg: String,
    },
};
</script>

