<template>
    <div class="hello">
        <img src='@/assets/logo-django.png' style="width: 250px" />
        <p>The data below is added/removed from the SQLite Database using Django's ORM and Rest Framework.</p>
        <br/>
        <p>Subject</p>
        <input type="text" placeholder="Hello" v-model="subject">
        <p>Message</p>
        <input type="text" placeholder="From the other side" v-model="msgBody">
        <p>Date</p>
        <input type="date" v-model="msgDate">
        <br><br>
        <button
                type="submit"
                @click="addMessage({ subject: subject, body: msgBody, date : msgDate })"
                :disabled="!subject || !msgBody || !msgDate"> add</button>

        <hr/>
        <h3>Messages on Database</h3>
        <p v-if="messages.length === 0">No Messages</p>
        <div class="msg" v-for="(msg, index) in messages" :key="index">
            <p class="msg-index">[{{index}}]</p>
            <p class="msg-subject" v-html="msg.subject"></p>
            <p class="msg-body" v-html="msg.body"></p>
            <p class="msg-date" v-html="msg.date"></p>
            <input type="submit" @click="deleteMessage(msg.pk)" value="Delete" />
        </div>
    </div>
</template>

<script>
    import { mapState, mapActions } from 'vuex'
    import Comments from "@/components/Comments.vue"

    export default {
        name: "Messages",
        data() {
            return {
                subject: "",
                msgBody: "",
                msgDate: "",
            };
        },
        computed: mapState({
            messages: state => state.messages.messages
        }),
        methods: mapActions('messages', [
            'addMessage',
            'deleteMessage'
        ]),
        created() {
            this.$store.dispatch('messages/getMessages')
        },
        components:{
            'blockComments':Comments
        },
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    hr {
        max-width: 65%;
    }

    .msg {
        margin: 0 auto;
        max-width: 30%;
        text-align: left;
        border-bottom: 1px solid #ccc;
        padding: 1rem;
    }

    .msg-index {
        color: #ccc;
        font-size: 0.8rem;
        /* margin-bottom: 0; */
    }

    img {
        width: 250px;
        padding-top: 50px;
        padding-bottom: 50px;
    }

</style>
