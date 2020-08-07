import Head from 'next/head'
import { FormControl, Input, InputLabel, FormHelperText} from '@material-ui/core'

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

export default function Home(props) {
  return (
    <div>
      	<Head>
        	<title>{String(props.user)}</title>
      	</Head>
      <h1>{props.user}</h1>
      <FormControl>
        <InputLabel htmlFor="my-input">Email address</InputLabel>
        <Input id="my-input" aria-describedby="my-helper-text" />
        <FormHelperText id="my-helper-text">We'll never share your email.</FormHelperText>
      </FormControl>
    </div>
  )
}
