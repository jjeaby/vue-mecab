<template>
    <div class="mecab">
        <div>
            <h1> This is meacab Servie </h1>
        </div>
        <div align="center">
            <div class="divTable">
                <div class="divTableBody">
                    <div class="divTableRow">
                        <div class="divTableCell">
                            <MultilineMsgBox msg="Welcome to Your Vue.js App"/>
                        </div>
                        <div class="divTableCell">
                            <img src="@/assets/arrow.png">
                        </div>
                        <div class="divTableCell">
                            <MultilineMsgBox msg="Welcome to Your Vue.js App"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import MultilineMsgBox from '@/components/MultilineMsgBox.vue';

    export default {
        name: 'mecabpos',
        components: {
            MultilineMsgBox,
        },
    };

</script>
