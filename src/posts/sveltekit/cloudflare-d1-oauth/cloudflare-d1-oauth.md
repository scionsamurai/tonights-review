---
title: Setting Up SvelteKit with Cloudflare Pages, D1 Storage, and OAuth
description: Dive into the world of SvelteKit and discover how to deploy your applications effortlessly using Cloudflare Pages. In this detailed blog post, we cover everything from creating a new SvelteKit project to configuring D1 storage and setting up GitHub OAuth authentication. Follow along with our step-by-step instructions and elevate your web development skills with this powerful tech stack.
date: 'Sat, 04 Aug 2024 12:37:03 GMT'
categories:
  - sveltekit
  - oauth
  - d1
  - cloudflare
author_id: 1
image: /images/cloudflare-d1-oauth-banner-png.png
webp_image: /images/cloudflare-d1-oauth-banner.webp
image_thumb: /images/cloudflare-d1-oauth-banner-png_thumb.png
banner_alt: "Image of Svelte's S logo perched ontop of a cloudflare cloud"
show_banner: true
comments: true
published: true
---
## Introduction

In today's rapidly evolving web development landscape, choosing the right tools and services can significantly impact your application's efficiency and performance. This guide will walk you through setting up a powerful and modern web application stack using SvelteKit, Cloudflare Pages, D1 storage, and OAuth authentication.

The completed code can be viewed on [github](https://github.com/scionsamurai/auth-sveltekit-cloudflare-pages).

### The Tech Stack

Let's break down the key components of our stack:

1. **SvelteKit**: A framework for building scalable web applications with a focus on speed and simplicity.
2. **Cloudflare Pages**: A JAMstack platform offering fast, secure hosting with continuous deployment from Git.
3. **Cloudflare D1**: A serverless SQL database running on Cloudflare's global network.
4. **OAuth**: An open standard for secure authentication, which we'll implement using GitHub as the provider.

### Why This Stack?

You might be wondering, "Why should I use this particular combination?" Here are some compelling reasons:

- **Lightning-Fast Performance**: SvelteKit's lean approach, combined with Cloudflare's global CDN, ensures your app loads in the blink of an eye.
- **Effortless Scalability**: From small projects to large-scale applications, Cloudflare Pages and D1 scale without breaking a sweat.
- **Developer-Friendly**: SvelteKit's intuitive model and Cloudflare's streamlined tools make development a breeze.
- **Rock-Solid Security**: OAuth authentication and Cloudflare's robust security features keep your app and user data safe.
- **Cost-Effective**: Pay only for what you use, thanks to the serverless nature of this stack.

### What You'll Learn

By the end of this tutorial, you'll know how to:

1. Set up a SvelteKit project with Cloudflare Pages
2. Configure and use Cloudflare D1 for data storage
3. Implement OAuth authentication with GitHub
4. Connect authentication to D1 for user management
5. Deploy your application to Cloudflare Pages

Whether you're building a personal project or a large-scale application, this stack provides a solid foundation for modern, performant web development. Let's dive in and start building!

## Prerequisites

Before we dive into the nitty-gritty of setting up our SvelteKit application with Cloudflare Pages, D1 storage, and OAuth, let's ensure you have everything you need to follow along smoothly.

### Required Accounts

To get started, you'll need to set up the following accounts:

1. **Cloudflare Account**: If you don't already have one, head over to [Cloudflare's website](https://www.cloudflare.com/) and sign up for a free account.

2. **GitHub Account**: We'll be using GitHub for OAuth authentication, so make sure you have a GitHub account. If you don't, you can create one at [GitHub's signup page](https://github.com/join).

### Essential Tools

Ensure you have the following tools installed on your local machine:

1. **Node.js and npm**: Our project relies on Node.js and npm (Node Package Manager). Install the latest LTS version from the [official Node.js website](https://nodejs.org/).

   To verify your installation, open your terminal and run:
   ```
   node --version
   npm --version
   ```

2. **Wrangler CLI**: Wrangler is Cloudflare's command-line tool for managing Workers and Pages projects. Install it globally using npm:
   ```
   npm install -g wrangler
   ```

   After installation, verify it's working:
   ```
   wrangler --version
   ```

### Development Environment

While not strictly necessary, we recommend using a code editor with good TypeScript and Svelte support. Some popular options include:

- [Visual Studio Code](https://code.visualstudio.com/) with the [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) extension
- [WebStorm](https://www.jetbrains.com/webstorm/)
- [Sublime Text](https://www.sublimetext.com/) with the [Svelte plugin](https://packagecontrol.io/packages/Svelte)

### Ready to Go!

With these prerequisites in place, you're all set to embark on your journey of building a modern web application with SvelteKit, Cloudflare Pages, D1 storage, and OAuth authentication. In the next section, we'll start by setting up our SvelteKit project and configuring it for Cloudflare Pages deployment.

Remember, if you encounter any issues during setup, don't hesitate to consult the official documentation for each tool or reach out to their respective community forums for support.

## Setting up the SvelteKit Project with Cloudflare

Alright, folks! It's time to roll up our sleeves and dive into the exciting part - setting up our SvelteKit project with Cloudflare. Let's turn those prerequisites into a real, living, breathing web application!

### Creating the Project

Let's start by creating our SvelteKit project using Cloudflare's CLI tool. This process might vary slightly depending on your preferences and any potential issues you might encounter.

1. Open your terminal and run the following command:
   ```
   npm create cloudflare@latest my-svelte-app -- --framework=svelte
   ```

2. Follow the prompts to customize your SvelteKit project. You can accept the defaults for now - we can always adjust things later.

3. Important note: During the setup process, you'll be asked if you want to deploy to Cloudflare Pages. 
   - If you prefer to use Git integration with Cloudflare Pages (recommended for better version control), choose "No" at this prompt.
   - If you choose "Yes", the project will be directly uploaded to Cloudflare Pages and you'll be able to skip the github/cloudflare deployment steps below.

4. The installation process might freeze for some users after "installing dependencies". If this happens to you:
   - Press CTRL+C to cancel the process
   - Navigate to your project directory:
     ```
     cd my-svelte-app
     ```
   - Delete the `node_modules` folder:
     ```
     rm -rf node_modules
     ```
   - Reinstall the dependencies:
     ```
     npm install
     ```

5. If the installation completed successfully without freezing, simply navigate to your new project directory:
   ```
   cd my-svelte-app
   ```

By following these steps, you'll have your SvelteKit project set up and ready for further development. If you chose not to deploy directly to Cloudflare Pages, you can set up Git integration later, allowing you to push your code to a Git repository and have Cloudflare Pages automatically deploy from there.


### Project Structure Deep Dive

Now that we've got our project set up, let's take a quick tour of what we're working with. Here's a bird's-eye view of our project structure:

```
my-sveltekit-app/
├── src/
│   ├── routes/
│   │   └── +page.svelte
│   ├── app.html
│   └── app.d.ts
├── static/
├── tests/
├── package.json
├── svelte.config.js
├── tsconfig.json
└── wrangler.toml
```

Let's break down some key files:

- `src/routes/+page.svelte`: This is your main page component. SvelteKit uses file-based routing, so this file represents your home page.
- `src/app.html`: The HTML template for your entire app.
- `svelte.config.js`: Configuration for SvelteKit and its adapter.
- `wrangler.toml`: Configuration for Cloudflare Workers and Pages.

### Cloudflare Configuration

Now, let's make sure our project is properly configured for Cloudflare:

1. Install adapter and open `svelte.config.js` to ensure it's using the Cloudflare adapter:
   ```
   npm install -D @sveltejs/adapter-cloudflare
   ```

   ```javascript
    import adapter from '@sveltejs/adapter-cloudflare';
    import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

    /** @type {import('@sveltejs/kit').Config} */
    const config = {
        preprocess: vitePreprocess(),

        kit: {
            adapter: adapter({
                routes: {
                    include: ['/*'],
                    exclude: ['<all>']
                }
            })
        }
    };

    export default config;
   ```

2. Check your `wrangler.toml` file. It should look something like this:

   ```toml
   name = "my-sveltekit-app"
   compatibility_date = "2024-08-04"
   ```

   Don't worry if some details are different - Cloudflare's CLI tool should have set this up correctly for you.

### Taking It for a Spin

Let's make sure everything's working as expected:

1. Start the development server:
   ```
   npm run dev
   ```

2. Open your browser and navigate to `http://localhost:5173`. Ideally we haven't broken anything yet and we can keep on rolling!

### Logging into Wrangler

Before we can deploy our app, we need to log in to Wrangler:

1. Run the following command:
   ```
   npx wrangler login
   ```

2. This will open a browser window. Follow the prompts to log in to your Cloudflare account.

3. Once logged in, you'll see a success message in your terminal.

## Deploying Your SvelteKit App to Cloudflare Pages

Let's deploy our SvelteKit app to Cloudflare Pages using GitHub. Follow these steps:

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in to your account.
2. Click on the "+" icon in the top right corner and select "New repository".
3. Enter a name for your repository (e.g., `your-repo-name`).
4. Optionally, add a description and choose whether to make it public or private.
5. Click "Create repository".

### Step 2: Push Your Project to GitHub

Now that you have a repository, you can push your SvelteKit project to it:

1. Open your terminal and navigate to your SvelteKit project directory.
2. Initialize a new Git repository and push your code:

   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

### Step 3: Deploy to Cloudflare Pages

1. Log in to your Cloudflare account and navigate to the "Workers & Pages" section.
2. Click "Create" and switch to the "Pages" tab.
3. Select "Connect to Git" and choose GitHub as your Git provider and authorize Cloudflare to access your repositories.
4. Select the repository you just created for your SvelteKit app.
5. Configure your build settings:
   - **Framework preset**: `SvelteKit`
   - **Build command**: `npm run build`
   - **Build output directory**: `.svelte-kit/cloudflare`
   - **Environment variables**: Add `NODE_VERSION` with a value of `20.13.1` (or your preferred Node.js version).
6. Click "Save and Deploy".

Cloudflare Pages will now build and deploy your application. Once the deployment is complete, you'll receive a URL where your app is live.

<script>
    import SummaryDetails from '$lib/components/SummaryDetails.svelte'
</script>
<SummaryDetails summary="HELP! My build fails due to a Node.js version incompatibility error!">

An example of this error is below.

```
npm ERR! code EBADENGINE
npm ERR! engine Unsupported engine
npm ERR! engine Not compatible with your version of node/npm: @eslint/config-array@0.17.1
npm ERR! notsup Not compatible with your version of node/npm: @eslint/config-array@0.17.1
npm ERR! notsup Required: {"node":"^18.18.0 || ^20.9.0 || >=21.1.0"}
npm ERR! notsup Actual:   {"npm":"9.6.7","node":"v18.17.1"}
```

Follow these steps to resolve it:

1. Click the "continue with failed deployment" button.
2. Go to the "Settings" page of your Cloudflare Pages project.
3. Scroll down to the "Environment variables" section.
4. Click on "Edit variables" for both "Production" and "Preview" environments.
5. Find the `NODE_VERSION` variable and update its value to a compatible version (e.g., `20.9.0` or higher).
6. Make sure to click the "Encrypt" checkbox next to the `NODE_VERSION` variable.
7. Save your changes.

</SummaryDetails>

### Step 4: Update Your App

Whenever you make changes to your project, follow these steps to update your app:

1. Commit and push your changes to GitHub:

   ```
   git add .
   git commit -m "Update app"
   git push
   ```

2. Cloudflare Pages will automatically detect the new commit and redeploy your app.

And there you have it! Your SvelteKit app is now live on Cloudflare Pages. In the next section, we'll set up our Cloudflare D1 database to add data persistence to our application. Keep up the great work!

## Configuring Cloudflare D1 Database

Alright, data enthusiasts! It's time to add some persistence to our SvelteKit app with Cloudflare D1. Buckle up, because we're about to turn our application into a data-driven powerhouse!

### What's D1, Anyway?

Before we dive in, let's quickly recap: D1 is Cloudflare's serverless SQL database. It's like having a turbo-charged SQLite database that lives on the edge. Cool, right?

### Creating Our D1 Database

First things first, let's create our database:

1. Log into your Cloudflare dashboard (if you haven't already).
2. Navigate to the "Workers & Pages" section.
3. Click on the "D1" tab.
4. Hit that "Create database" button!
5. Give your database a snazzy name. How about "my_sveltekit_db"?
6. Click "Create" and watch the magic happen!

### Connecting D1 to Our SvelteKit Project

Now comes the fun part - linking our shiny new database to our SvelteKit app.

1. Open your `wrangler.toml` file and add the following:

   ```toml
   [[d1_databases]]
   binding = "DB" # i.e. available in your Worker on env.DB
   database_name = "my_sveltekit_db"
   database_id = "<your-database-id>"
   ```

   Replace `<your-database-id>` with the actual ID from your Cloudflare dashboard.


2. Now, let's update our `src/app.d.ts` to include our database type:

   ```typescript
   /// <reference types="@cloudflare/workers-types" />

   // See https://kit.svelte.dev/docs/types#app
   // for information about these interfaces
   declare global {
     namespace App {
       // interface Error {}
       // interface Locals {}
       // interface PageData {}
       // interface Platform {}
       interface Platform {
         env: {
           DB: D1Database;
         };

        context: {
            waitUntil(promise: Promise<any>): void;
        };
        caches: CacheStorage & { default: Cache };    
       }
     }
   }

   export {};
   ```

### Setting Up Tables

Now that we have our database, let's give it some structure. We'll create a simple "users" table to store our authenticated users. If you want to run any of these commands on the remote server (non-dev) you can add the "--remote" flag to the commands.

1. In your terminal, run this command:

   ```
   npx wrangler d1 execute my_sveltekit_db --command "CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, name TEXT, image TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"

   ```

2. If all goes well, you should see a success message. Let's verify by checking our table:

   ```
   npx wrangler d1 execute my_sveltekit_db --command "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
   ```

   You should see your "users" table listed. High five! ✋

### Testing Our Database Connection

Let's make sure everything's connected properly by creating a simple API route to fetch users.

1. Create a new file `src/routes/api/users/+server.ts`:

   ```typescript
    import type { RequestHandler } from "@sveltejs/kit";

    /** @type {import('@sveltejs/kit').RequestHandler} */
    export async function GET({ request, platform }) {
    let result = await platform.env.DB.prepare(
        "SELECT * FROM users LIMIT 5"
    ).run();
    return new Response(JSON.stringify(result));
    }
   ```

2. Start your development server:

   ```
   npm run dev
   ```

3. Visit `http://localhost:5173/api/users` in your browser. You should see an empty array `[]` (since we haven't added any users yet), but no errors. That means we're connected!

## Implementing OAuth Authentication

Alright, security squad! It's time to add some street cred to our app with OAuth authentication. We're going to use GitHub as our OAuth provider, because who doesn't love a little social coding flair? Let's dive in and make our app as secure as Fort Knox, but way cooler!

### Setting Up GitHub OAuth

We'll set up two sets of GitHub OAuth credentials: one for local development and another for production.

#### Local Development Credentials:

1. Go to your GitHub account and navigate to Settings > Developer settings > OAuth Apps.
2. Click on "New OAuth App".
3. Fill in the details:
   - Application name: "My SvelteKit App (Development)"
   - Homepage URL: `http://localhost:5173`
   - Authorization callback URL: `http://localhost:5173/auth/callback/github`
4. Click "Register application".
5. Note down the Client ID and generate a new client secret.

#### Production Credentials:

1. Repeat the process, but use your production details:
   - Application name: "My SvelteKit App (Production)"
   - Homepage URL: `https://your-app-name.pages.dev` (your Cloudflare Pages domain)
   - Authorization callback URL: `https://your-app-name.pages.dev/auth/callback/github`
2. Register the application and note down the credentials.

### Installing the Auth Packages

Install the necessary authentication packages:

```
npm install @auth/core @auth/sveltekit
```

### Setting Up Environment Variables

For local development:

1. Create a `.env` file in your project root:

   ```
   GITHUB_ID=your_local_github_client_id
   GITHUB_SECRET=your_local_github_client_secret
   AUTH_SECRET=your_random_secret_here
   ```

   Replace the values with your local GitHub OAuth credentials. Generate `AUTH_SECRET` with `openssl rand -base64 32`.

2. Add `.env` to your `.gitignore` file.

For production deployment on Cloudflare Pages:

1. Open your `wrangler.toml` file and add the following:

   ```toml
   [vars]
   AUTH_SECRET = "your_production_auth_secret"
   AUTH_TRUST_HOST = "true"
   GITHUB_ID = "your_production_github_client_id"
   GITHUB_SECRET = "your_production_github_client_secret"
   ```

   Replace the values with your production GitHub OAuth credentials.

2. If your GitHub repository is public, consider setting it to private to protect your production credentials.

Alternatively, you can set these environment variables in the Cloudflare dashboard under your project's settings for added security.

By setting up separate OAuth credentials and using different configuration methods for local and production environments, you ensure a smooth development process and a secure production deployment.

### Configuring Authentication

Now, let's set up our authentication logic. We'll start with the basic GitHub OAuth setup and then add user-saving functionality later.

1. Create a new file `src/auth.ts`:

   ```typescript
    import { SvelteKitAuth } from "@auth/sveltekit";
    import GitHub from '@auth/sveltekit/providers/github';
    import { GITHUB_ID, GITHUB_SECRET, AUTH_SECRET } from '$env/static/private';

    export const { handle, signIn, signOut } = SvelteKitAuth(async (event) => {

        const getEnv = (key) => {
            if (event.platform?.env.CF_PAGES === 'true') {
                return event.platform?.env[key];
            } else {
                switch(key) {
                    case 'GITHUB_ID': return GITHUB_ID;
                    case 'GITHUB_SECRET': return GITHUB_SECRET;
                    case 'AUTH_SECRET': return AUTH_SECRET;
                    default: return undefined;
                }
            }
        };

        const authOptions = {
            providers: [
                GitHub({
                    clientId: getEnv('GITHUB_ID'),
                    clientSecret: getEnv('GITHUB_SECRET')
                })
            ],
            secret: getEnv('AUTH_SECRET'),
            trustHost: true,
        };

        return authOptions;
    });
   ```

   This file sets up the core authentication logic using SvelteKitAuth. It configures GitHub as the OAuth provider and handles environment variables for both development and production environments.

2. Update `src/hooks.server.ts`:

   ```typescript
   export { handle } from "./auth";
   ```

   This file exports the `handle` function from our auth configuration, which SvelteKit will use to process authentication for each request.

3. Create `src/routes/+layout.server.ts`:

   ```typescript
    import type { LayoutServerLoad } from './$types';
    import { dev } from '$app/environment';
    import { GITHUB_ID } from '$env/static/private';

    export const load: LayoutServerLoad = async (event) => {
        return {
            session: await event.locals.auth(),
            authProviders: {
                github: {
                    clientId: dev ? GITHUB_ID : event.platform?.env?.GITHUB_ID
                }
            }
        };
    };
   ```

   This layout server load function provides the session data and GitHub client ID to all routes in your app. It ensures that authentication state is available throughout your application.

4. Update `src/routes/+layout.svelte` to include login/logout buttons:

   ```svelte
   <script lang="ts">
     import { signIn, signOut } from "@auth/sveltekit/client";
     import { page } from "$app/stores";

     $: ({ session, authProviders } = $page.data);
   </script>

   <nav>
     {#if session}
       <span>Welcome, {session.user?.name}!</span>
       <button on:click={() => signOut()}>Sign out</button>
     {:else}
       <button on:click={() => signIn("github")}>Sign in with GitHub</button>
     {/if}
   </nav>

   <slot />
   ```

   This layout component provides a simple UI for signing in and out. It displays a welcome message and sign-out button when the user is authenticated, or a sign-in button when they're not.

### Testing GitHub Authentication

To make our development process smoother, let's add a custom script to our `package.json` file:

1. Open your `package.json` file and add the following script:

   ```json
   {
     "scripts": {
       // ... other scripts ...
       "dev:full": "npm run build && wrangler pages dev .svelte-kit/cloudflare --port 5173"
     }
   }
   ```

   This script combines the build process and starts the Wrangler Pages development server, making it easier to test our app with Cloudflare's environment.

2. Now, let's test our GitHub authentication:

   Start your development server using the new script:

   ```
   npm run dev:full
   ```

3. Visit `http://localhost:5173` in your browser and try logging in with GitHub. You should be able to authenticate successfully.

4. After logging in, you should see your GitHub name displayed and a sign-out button.

5. We can also push our file changes to github to test the production environment.

By using this `dev:full` script, we've simplified the process of starting our development server with Cloudflare's environment. This makes it easier to test features like authentication that might behave differently in a Cloudflare Pages context.

Remember, this setup uses your local development GitHub OAuth credentials. When you deploy to production, Cloudflare Pages will use the production credentials we set up earlier.



### Adding a User Profile Page

Let's create a profile page to display the user's information:

Create `src/routes/profile/+page.server.ts`:

```typescript
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async (event) => {
    const session = await event.locals.auth();
    return { user: session.user };
};
```

And `src/routes/profile/+page.svelte`:

```svelte
<script lang="ts">
    export let data;
    const { user } = data;
</script>

<h1>User Profile</h1>
<img src={user.image} alt={user.name} style="width: 100px; height: 100px; border-radius: 50%;" />
<p>Name: {user.name}</p>
<p>Email: {user.email}</p>
```

### Testing Our User Functionality

1. Start your development server:
   ```
   npm run dev:full
   ```

2. Visit `http://localhost:5173` and log in with GitHub.

3. After logging in, visit `http://localhost:5173/profile`. You should see your profile information, including the last login time.

### Protecting Routes

Want to keep some pages for authenticated users only? No problemo!

Create `src/routes/profile/+page.server.ts`:

```typescript
import { redirect } from '@sveltejs/kit'; // import this
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async (event) => {
  const session = await event.locals.auth();
  if (!session?.user) throw redirect(303, '/'); // and add this line
  return { user: session.user };
};
```

Or if we wanted to protect our `src/routes/api/users/+server.ts` route:

```typescript
import type { RequestHandler } from '@sveltejs/kit';
import { error, json } from '@sveltejs/kit';

export const GET: RequestHandler = async ({ locals, platform }) => {
    const session = await locals.auth();
    
    if (!session?.user) {
        throw error(401, 'Unauthorized');
    }

    try {
        const result = await platform.env.DB.prepare('SELECT * FROM users LIMIT 100').run();
        return json(result);
    } catch (err) {
        console.error('Database query error:', err);
        throw error(500, 'Internal Server Error');
    }
};
```

## Saving Authenticated Users in the Database

Let's dive into the nitty-gritty of saving our authenticated users to our D1 database. This is where the magic of persistence meets the power of authentication! Let's go through the setup:

1. Install `@auth/d1-adapter`:

   ```
   npm install next-auth @auth/d1-adapter
   ```

2. Update `src/auth.ts`:

```typescript
// ... previous imports ...
import { D1Adapter } from "@auth/d1-adapter";

export const { handle, signIn, signOut } = SvelteKitAuth(async (event) => {

    const getEnv = (key) => {
        // ... remains the same ...
    };

    const authOptions = {
        providers: [
            GitHub({
                clientId: getEnv('GITHUB_ID'),
                clientSecret: getEnv('GITHUB_SECRET')
            })
        ],
        secret: getEnv('AUTH_SECRET'),
        trustHost: true,
        adapter: D1Adapter(event.platform?.env.DB),
        session: {
            strategy: 'database',
            maxAge: 30 * 24 * 60 * 60, // 30 days
            updateAge: 24 * 60 * 60 // update session age every 24 hours
        },
        callbacks: {
            async signIn({ user, account, profile }) { // optionally define allowed email domains or specific email addresses
                
                const allowedEmails = ['@yahoo.com', '@company.com', 'specific.user@gmail.com'];
                
                const isAllowedEmail = allowedEmails.some(email => 
                    user.email.endsWith(email) || user.email === email
                );

                if (isAllowedEmail) {
                    return true; // Allow sign-in
                } else {
                    return false; // Deny sign-in
                }
            },
            async session({ session, token }) {
                // Include the user ID (sub) in the session
                if (token?.sub) {
                    session.user.id = token.sub;
                }
                return session;
            }
        }
    };

    return authOptions;
});
```

This updated configuration uses the `D1Adapter` to directly interact with your database for storing authentication information. It also sets up database sessions and includes a callback to add the user ID to the session information.

3. Initialize the database schema:

```sql
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS "sessions";
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS verification_tokens;

CREATE TABLE IF NOT EXISTS "accounts" (
  "id" TEXT NOT NULL,
  "userId" TEXT NOT NULL DEFAULT NULL,
  "type" TEXT NOT NULL DEFAULT NULL,
  "provider" TEXT NOT NULL DEFAULT NULL,
  "providerAccountId" TEXT NOT NULL DEFAULT NULL,
  "refresh_token" TEXT DEFAULT NULL,
  "access_token" TEXT DEFAULT NULL,
  "expires_at" INTEGER DEFAULT NULL,
  "token_type" TEXT DEFAULT NULL,
  "scope" TEXT DEFAULT NULL,
  "id_token" TEXT DEFAULT NULL,
  "session_state" TEXT DEFAULT NULL,
  "oauth_token_secret" TEXT DEFAULT NULL,
  "oauth_token" TEXT DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS "sessions" (
  "id" TEXT NOT NULL,
  "sessionToken" TEXT NOT NULL,
  "userId" TEXT NOT NULL DEFAULT NULL,
  "expires" DATETIME NOT NULL DEFAULT NULL, 
  PRIMARY KEY (sessionToken)
);

CREATE TABLE IF NOT EXISTS "users" (
  "id" TEXT NOT NULL DEFAULT '',
  "name" TEXT DEFAULT NULL,
  "email" TEXT DEFAULT NULL,
  "emailVerified" DATETIME DEFAULT NULL,
  "image" TEXT DEFAULT NULL, 
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS "verification_tokens" (
  "identifier" TEXT NOT NULL,
  "token" TEXT NOT NULL DEFAULT NULL,
  "expires" DATETIME NOT NULL DEFAULT NULL, 
  PRIMARY KEY (token)
);
```

Before using this new method, you need to set up the required tables in your database. Save these commands to a file named "update_users_schema.sql" and then run the following command using Wrangler to execute the SQL file:

   ```
   npx wrangler d1 execute my_sveltekit_db --file update_users_schema.sql
   ```


These SQL commands create the necessary tables for storing authentication data, including user accounts, sessions, and verification tokens.

With these updates, your application will now store OAuth information directly in your database using the `@auth/d1-adapter`. This approach simplifies the authentication process and eliminates the need for a custom user-saving function.

### Testing Our Authentication

1. Start your development server:

   ```
   npm run dev:full
   ```

2. Visit `http://localhost:5173` and try logging in with GitHub.
3. After logging in, check your D1 database:

   ```
   npx wrangler d1 execute my_sveltekit_db --command "SELECT * FROM users"
   ```

4. To further verify, navigate to `localhost:5173/api/users` in your browser.
5. You should see your user information displayed, confirming that the data was successfully saved to the database.

   You should see your user info stored in the database. How cool is that?

## Conclusion: Your SvelteKit App is Ready to Conquer the Web!

Well, folks, we've been on quite the journey together! From setting up our SvelteKit project to implementing OAuth, and wrangling our D1 database. Let's take a moment to bask in the glory of what we've accomplished:

1. We've set up a blazing-fast SvelteKit application
2. Implemented secure OAuth authentication with GitHub
3. Stored and managed user data with Cloudflare's D1 database

### What's Next?

The sky's the limit! Here are some ideas to take your app to the next level:

- Implement additional OAuth providers (Google, Facebook, Twitter, etc.)
- Create a user dashboard with personalized content
- Add more real-time features like live chat or collaborative editing
- Implement server-side rendering (SSR) for improved SEO
- Optimize your app's performance using Cloudflare's analytics

### Final Thoughts

Building modern web applications doesn't have to be a headache. With SvelteKit, D1, and  Cloudflare Pages, we've created a powerful, scalable, and real-time capable application without breaking a sweat (okay, maybe a little sweat, but it was worth it!).

Remember, the best apps are those that continue to evolve. Keep learning, keep experimenting, and most importantly, keep having fun with it!

You've now got a solid foundation in some of the most exciting web technologies out there. So go forth and build amazing things! Who knows? Your next project could be the next big thing on the web.

### Additional Resources

To help you continue your journey and dive deeper into the technologies we've used, here are some valuable resources:

1. **[SvelteKit Documentation](https://kit.svelte.dev/docs)**: The official docs are your best friend for all things SvelteKit.

2. **[Cloudflare Pages Documentation](https://developers.cloudflare.com/pages/)**: Learn more about deploying and optimizing your sites on Cloudflare Pages.

3. **[Cloudflare D1 Documentation](https://developers.cloudflare.com/d1/)**: Dive deeper into D1's capabilities and advanced querying techniques.

4. **[Durable Objects Documentation](https://developers.cloudflare.com/workers/learning/using-durable-objects/)**: Explore more ways to leverage Durable Objects for stateful applications.

5. **[Auth.js Documentation](https://authjs.dev/)**: Discover more authentication providers and advanced configurations.

6. **[Svelte Society](https://sveltesociety.dev/)**: Join the Svelte community, find resources, and stay updated with the latest in Svelte ecosystem.

7. **[Cloudflare Workers Discord](https://discord.gg/cloudflaredev)**: Connect with other developers and get help with Cloudflare-specific questions.

