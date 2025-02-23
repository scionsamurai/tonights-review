import { dev } from '$app/environment'

export const siteName = 'TonightsReview'
export const description = 'SvelteKit blog for poets'
export const url = dev ? 'http://localhost:5173/' : 'https://www.tonightsreview.com/'
export const email = "admin@tonightsreview.com"


export let createSlug = (blogTitle) => {
    // Convert to lowercase and replace spaces with %20
    const encodedSlug = blogTitle.toLowerCase().replace(/\s+/g, '%20');
  
    // Remove other special characters
    const cleanSlug = encodedSlug.replace(/[^\w%20]+/g, '');
  
    return cleanSlug;
  }