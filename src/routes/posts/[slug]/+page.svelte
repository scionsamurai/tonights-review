<script>
	import { onMount } from 'svelte'
	import { updateCopyLinks, closeShareLinks, closeMobileTableOfContents } from '../post.js'
	import Sharelinks from '../sharelinks.svelte'
	import MobileShareLinks from '../MobileShareLinks.svelte'
	import SEO from '../SEO.svelte'
	import PostHeader from '../PostHeader.svelte'
	import TableOfContents from '$lib/components/TableOfContents.svelte'
	import AuthorInfo from '../AuthorInfo.svelte'
	import Comments from '../Comments.svelte'
	import Contribute from '../Contribute.svelte'

	import '../post.css'

	export let data

    const githubLink = data.meta.group 
        ? `https://github.com/scionsamurai/tonights-review/tree/main/src/posts/${data.meta.group}/${data.slug}/${data.slug}.md`
        : `https://github.com/scionsamurai/tonights-review/tree/main/src/posts/${data.slug}/${data.slug}.md`


	onMount(() => {
		updateCopyLinks()
		closeMobileTableOfContents()
		closeShareLinks()

		document.querySelectorAll('h2, h3').forEach((header) => {
			if (header.classList.contains('dont-link')) return
			const link = document.createElement('a')
			link.className = 'header-link'
			link.innerHTML = '#'
			link.href = `#${header.id}`
			header.appendChild(link)
		})
	})
</script>

<SEO {data} />

<div role="main" class="main-content">
	<div class="post-container">
		<article class="post">
			{#if !data.meta.published}
				<p class="draft">Draft Warning: Until published these are minimally organized notes for {data.author.name}!</p>
			{/if}
			<PostHeader meta={data.meta} />
			<svelte:component this={data.content} slug={data.slug} />
			<MobileShareLinks
				post_title={data.meta.title}
				image_path={data.meta.image}
				post_slug={data.slug}
			/>
			<Contribute {githubLink} />
			{#if data.meta.comments}
				<Comments />
			{/if}
		</article>
		<Sharelinks post_slug={data.slug} post_title={data.meta.title} image_path={data.meta.image} />
	</div>
	<aside class="sidebar">
		<AuthorInfo author={data.author} />
		<TableOfContents headers={data.meta.headers} />
	</aside>
</div>

<style lang="scss">
	@import 'src/styles/Post.scss';
</style>
