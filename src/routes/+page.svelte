<script lang="ts">
	import * as config from '$lib/config'
	import Banner from '$lib/ui/banner.svelte'
	import PostSection from '$lib/ui/post_section/section.svelte'
    import Pagination from '$lib/ui/Pagination.svelte';

	export let data;
    const { posts, pagination } = data;
</script>

<svelte:head>
	<title>{config.siteName}</title>
</svelte:head>

<Banner h1_text="Welcome!" p_text="Honest opinions and thoughtful insights on everything worth your attention." />

 <PostSection posts={posts} />

 <Pagination currentUrl={data.url} page={pagination.page} totalPages={pagination.totalPages} />