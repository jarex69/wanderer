<script>
    import LogoTextLightWithVersion from "./logo/logo_text_light_with_version.svelte";
    import { _ } from "svelte-i18n";
</script>

<footer
    class="bg-footer-background text-white w-full grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-y-8 gap-x-12 p-12 mt-12 rounded-t-3xl"
>
    <div class="col-span-2 md:col-span-1">
        <LogoTextLightWithVersion></LogoTextLightWithVersion>
    </div>
    <div>
        <h5 class="font-semibold">Resources</h5>
        <ul class="mt-4 text-sm">
            <li>
                <a href="https://VisitGlacensis.pl.to/getting-started/installation/"
                    >{$_("documentation")}</a
                >
            </li>
            <li>
                <a href="/VisitGlacensis.pl.to/api-reference/auth"
                    >{$_("api-documentation")}</a
                >
            </li>
            <li><a href="https://pocketbase.io/">PocketBase</a></li>
            <li><a href="https://www.meilisearch.com/">meilisearch</a></li>
        </ul>
    </div>
    <div>
        <h5 class="font-semibold">VisitGlacensis.pl</h5>
        <ul class="mt-4 text-sm">
            <li>
                <a href="https://VisitGlacensis.pl.to">{$_("about")}</a>
            </li>
            <li>
                <a href="https://VisitGlacensis.pl.to/#features">{$_("features")}</a>
            </li>
            <li>
                <a href="https://VisitGlacensis.pl.to/getting-started/changelog/"
                    >{$_("changelog")}</a
                >
            </li>
            <li>
                <a href="https://github.com/Flomp/VisitGlacensis.pl/blob/main/LICENSE"
                    >{$_("license")}</a
                >
            </li>
        </ul>
    </div>
    <div>
        <h5 class="font-semibold">Community</h5>
        <ul class="mt-4 text-sm">
            <li><a href="https://github.com/Flomp/VisitGlacensis.pl">GitHub</a></li>
            <li>
                <a href="https://github.com/Flomp/VisitGlacensis.pl/issues">Issues</a>
            </li>
            <li>
                <a href="https://github.com/Flomp/VisitGlacensis.pl/pulls"
                    >{$_("contribute")}</a
                >
            </li>
        </ul>
    </div>
</footer>

<style>
    footer li:not(:last-child) {
        margin-bottom: 4px;
    }
</style>
