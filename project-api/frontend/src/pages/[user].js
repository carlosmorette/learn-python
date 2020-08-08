import Head from 'next/head'

export async function getStaticPaths() {
    return {
        paths: [],
        fallback: true
    }
}

export async function getStaticProps(context) {
    const { user } = context.params
    return {
        props: {
            user
        }
    }
}

async function getUserGitHub(name) {
    const response = await fetch(`https://api.github.com/users/${name}`).then(resp => resp.json()).then(data => data)
    return {
        login: response.login,
        avatar_url: response.avatar_url,
        bio: response.bio,
        company: response.company
    }
}

export default function Home(props) {


    const login = getUserGitHub(props.name)
    console.log(login)

    return (
        <div>
            <Head>
                <title>{String(props.user)}</title>
                <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600&display=swap" rel="stylesheet" />
            </Head>
            <h1 style={{ fontFamily: "Montserrat" }}>{props.user}</h1>
            {
                <div>
                </div>
            }
        </div>
    )
}
