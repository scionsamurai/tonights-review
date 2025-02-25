<script lang="ts">
	import * as config from '$lib/config'
</script>

<!-- Footer -->
<footer>
	<div class="footer-content">
		<div class="footer-section">
			<h4 class="dont-link">About</h4>
			<p>
				Welcome to Tonights Review - your trusted source for comprehensive product reviews,
				honest opinions, and in-depth analysis to help you make informed decisions.
			</p>
		</div>
		<div class="footer-section">
			<h4 class="dont-link">Contact</h4>
			<a href={`mailto:${config.email}`}>{config.email}</a>
		</div>
		<ul class="footer-section">
			<li><a href="/rss.xml" target="_blank">RSS</a></li>
			<li><a href="/sitemap">Sitemap</a></li>
			<li><a href="/about-us">About Us</a></li>
			<li><a href="/privacy-policy">Privacy Policy</a></li>
			<li><a href="/terms-of-service">Terms of Service</a></li>
		</ul>
		<p class="footer-disclaimer">
			<strong>Disclaimer:</strong> All content is provided for informational purposes only. While we 
			strive for accuracy in our reviews, we cannot guarantee the completeness or reliability of the information. 
			Product experiences may vary, and readers should conduct their own research before making purchase decisions.
		</p>

		<p class="footer-bottom">{config.siteName} &copy {new Date().getFullYear()}</p>
	</div>
</footer>

<style>
	footer {
		padding-block: var(--size-7);
	}

	p {
		color: var(--text-2);
	}
	/* Common styles */
	footer {
		background: var(--background-color-second);
		position: relative;
		z-index: 2;
		padding: 20px;
		text-align: center;
	}

	.footer-content {
		display: flex;
		justify-content: space-around;
		flex-wrap: wrap;
		margin-bottom: 20px;
	}

	.footer-section {
		flex-basis: 25%;
		padding: 10px;
	}

	.footer-section h4 {
		font-size: 16px;
		margin-bottom: 10px;
	}

	.footer-bottom {
		font-size: 14px;
	}

	.footer-bottom:before {
		display: inline-block;
		margin-right: 5px;
	}

	a {
		text-decoration: none;
	}

	a:hover {
		text-decoration: underline;
	}

	/* Responsive styles */
	@media screen and (max-width: 768px) {
		.footer-section {
			flex-basis: 50%;
		}
	}
	@media screen and (max-width: 480px) {
		.footer-section {
			flex-basis: 100%;
		}
	}
</style>
