import {reactive} from "vue";

export const store = reactive({
    users: [
        {
            name: 'Emily Cook',
            photo: '/src/assets/icons/girl.svg',
            online: true,
            status: 'Hi i am using dj chat',
            messages: [
                {
                    text: 'This is message',
                    read: true,
                    date_time: 'Yesterday',
                    sender_id: 'me'
                },
                {
                    text: 'This is message',
                    read: true,
                    date_time: 'Yesterday',
                    sender_id: 'him'
                }
            ]
        }
    ],
    selected_user: null
})